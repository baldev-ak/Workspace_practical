from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager as portal_pager


class MainGames(http.Controller):
    @http.route('/my/games', type='http', auth="user", website=True)
    def Games(self, page=1, date_begin=None, date_end=None, sortby=None, **kwargs):
        partner = request.env.user.partner_id
        game_user = partner.user_id
        values = {
            'game_user': game_user,
            'page_name': 'games',
        }
        games_collection = request.env['game.game']
        # make pager
        games_count = request.env['game.game'].search_count([])
        pager = portal_pager(
            url="/my/games",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=games_count,
            page=page,
            # step=self._items_per_page
        )
        # search the count to display, according to the pager data
        games = games_collection.search(([]))
        print("===================games", games)
        values.update({
            'date': date_begin,
            'games': games.sudo(),
            'page_name': 'games',
            'pager': pager,
            'default_url': '/my/games',
            # 'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render('Motivation.games_template_custom', values)

    @http.route('/my/games/<model("game.game"):game_obj>/', type='http', auth="public", website=True)
    def CRM(self, game_obj, **kwargs):
        return request.render('Motivation.games_template_custom_views', {'games': game_obj})
